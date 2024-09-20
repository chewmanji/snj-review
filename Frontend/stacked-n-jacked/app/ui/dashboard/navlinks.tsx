"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import clsx from "clsx";
import {
  House,
  BadgeCheck,
  Dumbbell,
  Award,
  CircleUserRound,
  LogOut,
} from "lucide-react";

const links = [
  { name: "Home", href: "/dashboard", icon: House },
  {
    name: "Exercises",
    href: "/dashboard/exercises",
    icon: Dumbbell,
  },
  { name: "Sessions", href: "/dashboard/sessions", icon: BadgeCheck },
  { name: "Your exercises", href: "/dashboard/user_exercises", icon: Award },
];

export default function NavLinks() {
  const pathname = usePathname();
  const accoutnHref = "/dashboard/account";

  return (
    <div className="flex grow flex-row justify-between space-x-2 md:flex-col md:space-x-0 md:space-y-2">
      {links.map((link) => {
        const LinkIcon = link.icon;
        return (
          <Link
            key={link.name}
            href={link.href}
            className={clsx(
              "flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-600 p-3 text-sm font-medium hover:bg-sky-100 hover:text-black md:flex-none md:justify-start md:p-2 md:px-3",
              {
                "bg-yellow-600 text-yellow-200": pathname === link.href,
              }
            )}
          >
            <LinkIcon className="w-6" />
            <p className="hidden md:block">{link.name}</p>
          </Link>
        );
      })}
      <div className="hidden h-auto w-full grow rounded-md bg-black md:block"></div>
      <Link
        href={accoutnHref}
        className={clsx(
          "flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-600 p-3 text-sm font-medium hover:bg-sky-100 hover:text-black md:flex-none md:justify-start md:p-2 md:px-3",
          {
            "bg-yellow-600 text-yellow-200": pathname === accoutnHref,
          }
        )}
      >
        <CircleUserRound />
        <p className="hidden md:block">Account</p>
      </Link>
      <form>
        <button className="flex h-[48px] w-full grow items-center justify-center gap-2 rounded-md bg-gray-600 p-3 text-sm font-medium hover:bg-sky-100 hover:text-black md:flex-none md:justify-start md:p-2 md:px-3">
          <LogOut />
          <div className="hidden md:block">Sign Out</div>
        </button>
      </form>
    </div>
  );
}