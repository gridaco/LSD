import React from "react";
import Image from "next/image";
import styled from "@emotion/styled";
import Link from "next/link";
import { motion } from "framer-motion";

export function HomeHeader({
  left,
  right,
}: {
  left?: React.ReactNode;
  right?: React.ReactNode;
}) {
  return (
    <HeaderWrapper>
      <motion.div
        initial={{
          opacity: 0,
          y: 10,
        }}
        animate={{
          opacity: 1,
          y: 0,
        }}
        transition={{
          delay: 0.4,
        }}
      >
        <Link href="/">
          <Image
            src="/lsd/lsd.png"
            alt="Logo"
            className="logo home"
            width={52}
            height={32}
            priority
          />
        </Link>
      </motion.div>
      <motion.div
        className="left"
        initial={{
          opacity: 0,
          y: 10,
        }}
        animate={{
          opacity: 1,
          y: 0,
        }}
        transition={{
          delay: 0.5,
        }}
      >
        {left}
      </motion.div>
      <motion.div
        initial={{
          opacity: 0,
          y: 10,
        }}
        animate={{
          opacity: 1,
          y: 0,
        }}
        transition={{
          delay: 0.5,
        }}
        className="right"
      >
        {right}
      </motion.div>
      {/* <div className="menu">
        <Link href="/crystal">
          <span className="item">CRYSTAL</span>
        </Link>
        <Link href="/acid">
          <span className="item">ACID</span>
        </Link>
        <Link href="/grass">
          <span className="item">GRASS</span>
        </Link>
      </div>
      <Link href="/rehab">
        <span>REHAB</span>
      </Link> */}
    </HeaderWrapper>
  );
}

export function HeaderSpace({ extra = 0 }: { extra?: number }) {
  return <div style={{ height: 68 + extra }} />;
}

const HeaderWrapper = styled.header`
  z-index: 10;
  width: 100%;
  position: fixed;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  padding-top: 24px;
  background: rgba(0, 0, 0, 0.01);
  backdrop-filter: blur(24px);

  .home {
    cursor: pointer;
  }

  .left {
    position: absolute;
    top: 24px;
    left: 24px;
  }

  .right {
    position: absolute;
    top: 24px;
    right: 24px;
  }

  .menu {
    margin-left: 80px;
    display: flex;
    flex-direction: row;
    gap: 16px;
    font-size: 16px;
  }

  .menu .item {
    opacity: 0.8;
    font-family: "Inter", sans-serif;
  }
`;
